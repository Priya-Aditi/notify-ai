import { useState } from "react";

import { analyzeMessage } from "../services/api";


interface AnalyzeMessageProps {
  onAnalyzed: () => void;
}


function AnalyzeMessage({
  onAnalyzed
}: AnalyzeMessageProps) {

  const [message, setMessage] = useState("");

  const [loading, setLoading] = useState(false);

  const [error, setError] = useState<string | null>(null);


  async function handleAnalyze() {

    if (!message.trim()) {
      setError("Please enter a message.");
      return;
    }


    try {

      setLoading(true);

      setError(null);


      await analyzeMessage(message);


      setMessage("");

      onAnalyzed();

    } catch (err) {

      console.error(err);

      setError("Unable to analyze the message.");

    } finally {

      setLoading(false);

    }
  }


  return (
    <div className="analyze-panel">

      <div className="analyze-header">

        <div>

          <h2>
            Analyze a Message
          </h2>

          <p>
            Let NotifyAI decide how important this message is.
          </p>

        </div>

      </div>


      <textarea
        value={message}
        onChange={(event) =>
          setMessage(event.target.value)
        }
        placeholder="Paste a notification, email, message, or reminder here..."
        rows={6}
      />


      {error && (
        <p className="analyze-error">
          {error}
        </p>
      )}


      <div className="analyze-actions">

        <button
          className="analyze-button"
          onClick={handleAnalyze}
          disabled={loading}
        >

          {loading
            ? "Analyzing..."
            : "Analyze Message"}

        </button>

      </div>

    </div>
  );
}


export default AnalyzeMessage;