// Trial file

const { spawn } = require("child_process");

const pythonProcess = spawn("python", ["dummy.py"]);

pythonProcess.stdout.on("data", (data) => {
  const outputText = data.toString().trim();
  if (outputText !== 0) {
    getAiResponse(outputText);
  }
});

// function myMethod(text) {
//   console.log(`Received output text: ${text}`);
// }

const { Configuration, OpenAIApi } = require("openai");
require('dotenv').config();

const apiKey = process.env.OPENAI_API_KEY;

const configuration = new Configuration({
  apiKey: apiKey,
});

async function getAiResponse(topic) {
  const openai = new OpenAIApi(configuration);
  const completion = await openai.createCompletion({
    model: "text-davinci-003",
    prompt: "You are a therapist. Answer like a therapist who cares about their patients." + topic,
    max_tokens: 1024,
    n: 1,
    stop: null,
    temperature: 0.7
  });
  console.log(completion.data.choices[0].text);
}