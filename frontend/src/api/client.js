const BASE_URL = process.env.REACT_APP_API_URL || "http://localhost:8000/api";

async function post(path, body) {
  const res = await fetch(`${BASE_URL}${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  if (!res.ok) throw new Error(`Request failed: ${res.status}`);
  return res.json();
}

export const analyzeText = (content) => post("/analyze/text", { content });
export const analyzeUrl = (url) => post("/analyze/url", { url });
