import React, { useState } from "react";
import { analyzeText } from "./api/client";

export default function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  async function handleAnalyze() {
    setLoading(true);
    setError(null);
    try {
      const data = await analyzeText(text);
      setResult(data);
    } catch (err) {
      setError("Could not reach the backend. Is it running on port 8000?");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div style={{ maxWidth: 640, margin: "40px auto", fontFamily: "sans-serif" }}>
      <h1>ScamShield AI</h1>
      <p>Paste a message below to check its scam risk.</p>
      <textarea
        rows={5}
        style={{ width: "100%" }}
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Paste SMS / WhatsApp / email text..."
      />
      <button onClick={handleAnalyze} disabled={loading || !text.trim()}>
        {loading ? "Analyzing..." : "Analyze"}
      </button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {result && (
        <div style={{ marginTop: 20, padding: 16, border: "1px solid #ccc" }}>
          <p><strong>Risk level:</strong> {result.risk_level}</p>
          <p><strong>Score:</strong> {result.risk_score}%</p>
          <p><strong>Category:</strong> {result.category}</p>
          <ul>
            {result.reasons.map((r, i) => <li key={i}>{r}</li>)}
          </ul>
          <p><strong>Recommendation:</strong> {result.recommendation}</p>
        </div>
      )}
    </div>
  );
}
