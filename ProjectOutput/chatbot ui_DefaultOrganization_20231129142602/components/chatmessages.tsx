import React from 'react';
interface ChatMessagesProps {
  chatMessages: string[];
}
const ChatMessages: React.FC<ChatMessagesProps> = ({ chatMessages }) => {
  return (
    <div className="p-4 overflow-y-auto">
      <div className="flex flex-col space-y-2">
        {chatMessages.map((message, index) => (
          <div key={index} className="bg-gray-100 rounded-md p-2">
            <p className="text-gray-800">{message}</p>
          </div>
        ))}
      </div>
    </div>
  );
};
export default ChatMessages;