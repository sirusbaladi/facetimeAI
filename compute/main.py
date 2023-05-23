import signal
import time
from vocode.streaming.input_device.base_input_device import BaseInputDevice
from vocode.helpers import create_microphone_input_and_speaker_output
from vocode.streaming.models.transcriber import (
    DeepgramTranscriberConfig,
    PunctuationEndpointingConfig,
)
from vocode.streaming.transcriber.base_transcriber import BaseTranscriber, Transcription
from vocode.streaming.transcriber.deepgram_transcriber import DeepgramTranscriber

if __name__ == "__main__":
    import asyncio
    from dotenv import load_dotenv

    load_dotenv()

    async def listen():
        async def on_response(response: Transcription):
            if response.is_final:
                with open('output.txt', 'w') as f:
                    f.write(response.message)

                return response.message

        microphone_input, speaker_output = create_microphone_input_and_speaker_output(
                streaming=True, use_default_devices=True
        )

        # replace with the transcriber you want to test
        # transcriber = DeepgramTranscriber(
        #     DeepgramTranscriberConfig.from_input_device(
        #         microphone_input, endpointing_config=PunctuationEndpointingConfig()
        #     )

        # )

        transcriber = DeepgramTranscriber(
            DeepgramTranscriberConfig(
            sampling_rate=44100,
            audio_encoding="linear16",
            chunk_size=1,
            endpointing_config=PunctuationEndpointingConfig(time_cutoff_seconds=0.4), 
            downsampling=None,
            min_interrupt_confidence=None,
            language=None, 
            model=None, 
            tier=None, 
            version=None,
            keywords=None,
            )
        )


        transcriber.set_on_response(on_response)
        asyncio.create_task(transcriber.run())
        print("Start speaking...press Ctrl+C to end. ")

        while True:
            chunk = microphone_input.get_audio()
            if chunk:
                transcriber.send_audio(chunk)
            await asyncio.sleep(0)

    asyncio.run(listen())