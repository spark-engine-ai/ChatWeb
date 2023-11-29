import React from 'react';
import Link from 'next/link';
const Footer = () => {
  return (
    <footer className="bg-gray-800 text-white py-4">
      <div className="container mx-auto flex justify-between items-center">
        <ul className="flex space-x-4">
          <li>
              <a className="hover:text-gray-300">
                Link 1
              </a>
          </li>
          <li>
              <a className="hover:text-gray-300">
                Link 2
              </a>
          </li>
          <li>
              <a className="hover:text-gray-300">
                Link 3
              </a>
          </li>
        </ul>
        <p>&copy; 2022 Your Company. All rights reserved.</p>
      </div>
    </footer>
  );
};
export default Footer;