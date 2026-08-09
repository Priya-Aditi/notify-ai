import type { Message } from "../types/message";


interface MessageCardProps {
  message: Message;
}


function MessageCard({ message }: MessageCardProps) {

const priorityMap: Record<string, string> = {
  P0: "critical",
  P1: "high",
  P2: "normal",
  P3: "low",
};


const priorityClass =
  priorityMap[message.priority ?? "P3"] ?? "low";


  return (
    <div className={`message-card ${priorityClass}`}>

      <div className="message-indicator"></div>


      <div className="message-content">

        <div className="message-top">

          <span
            className={`priority-badge ${priorityClass}-badge`}
          >
            {message.priority_label ?? "Low"}
          </span>


          <span className="message-time">
            {new Date(message.created_at).toLocaleString()}
          </span>

        </div>


        <h3>
          {message.summary ?? message.message}
        </h3>


        <p>
          {message.message}
        </p>


        <div className="message-meta">

          {message.category && (
            <span>
              📂 {message.category}
            </span>
          )}


          {message.requires_action && (
            <span>
              ⚡ Action required
            </span>
          )}

        </div>

      </div>

    </div>
  );
}


export default MessageCard;