import express from "express";
import cors from "cors";
import { openAI, chatCompletionRequest } from "./openai.js";
import { getFruits } from "./externalApi.js";
import { getAnimals } from "./externalApi.js";
import { getPrompts } from "./prompts.js";

const app = express();
const port = 3000;

// Middleware
app.use(cors());
app.use(express.json());

// Routes
app.post("/", async (req, res) => {
  const { prompt } = req.body;

  const messages = [];
  messages.push(getPrompts().componentBuilder);
  messages.push({ role: "user", content: prompt });
  const response = await chatCompletionRequest(messages);
  res.status(201).json(response);
});

// Server
app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});
