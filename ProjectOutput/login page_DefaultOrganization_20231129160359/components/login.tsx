// components/login.tsx
import React, { useState } from 'react';
const Login: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const handleEmailChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setEmail(e.target.value);
  };
  const handlePasswordChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setPassword(e.target.value);
  };
  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    // Handle login logic here
    console.log('Login:', email, password);
  };
  return (
    <form onSubmit={handleSubmit}>
      <div className="mb-4">
        <label htmlFor="email" className="block mb-2 font-bold">
          Email
        </label>
        <input
          type="email"
          id="email"
          className="w-full border border-gray-300 rounded px-3 py-2"
          value={email}
          onChange={handleEmailChange}
        />
      </div>
      <div className="mb-4">
        <label htmlFor="password" className="block mb-2 font-bold">
          Password
        </label>
        <input
          type="password"
          id="password"
          className="w-full border border-gray-300 rounded px-3 py-2"
          value={password}
          onChange={handlePasswordChange}
        />
      </div>
      <button
        type="submit"
        className="w-full bg-blue-500 text-white py-2 px-4 rounded"
      >
        Login
      </button>
    </form>
  );
};
export default Login;