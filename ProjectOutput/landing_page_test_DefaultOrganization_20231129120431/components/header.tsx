import React from 'react';
import Link from 'next/link';
const Header = () => {
  return (
    <header className="bg-gray-800 text-white py-4">
      <nav className="container mx-auto flex justify-between items-center">
          <a className="text-lg font-bold">
            Logo
          </a>
        <ul className="flex space-x-4">
          <li>
              <a className="hover:text-gray-300">
                Home
              </a>
          </li>
          <li>
              <a className="hover:text-gray-300">
                About
              </a>
          </li>
          <li>
              <a className="hover:text-gray-300">
                Services
              </a>
          </li>
          <li>
              <a className="hover:text-gray-300">
                Contact
              </a>
          </li>
        </ul>
      </nav>
    </header>
  );
};
export default Header;