/**
 * This component represents the landing page of the website.
 * It displays the main content and styling using Tailwind CSS.
 */
import React from 'react';
const LandingPage = () => {
  return (
    <div className="bg-gray-200">
      <header className="bg-blue-500 text-white py-4">
        <h1 className="text-4xl text-center">Welcome to Our Website</h1>
      </header>
      <main className="container mx-auto py-8">
        <h2 className="text-2xl mb-4">About Us</h2>
        <p className="text-lg">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed
          vestibulum, nisl in tincidunt aliquet, justo metus lacinia metus,
          vitae consequat nunc ex ac nunc. Nulla facilisi. Sed nec nisl
          vestibulum, lacinia est quis, aliquam nisl. Sed id ex auctor,
          ullamcorper nunc non, lacinia ligula. Sed ut lectus ut nunc
          tincidunt pellentesque. Sed auctor, nunc sed aliquet tincidunt,
          enim mi lacinia erat, vitae lacinia nunc enim vitae nunc. Sed
          vestibulum, nisl in tincidunt aliquet, justo metus lacinia metus,
          vitae consequat nunc ex ac nunc. Nulla facilisi. Sed nec nisl
          vestibulum, lacinia est quis, aliquam nisl. Sed id ex auctor,
          ullamcorper nunc non, lacinia ligula. Sed ut lectus ut nunc
          tincidunt pellentesque.
        </p>
      </main>
      <footer className="bg-blue-500 text-white py-4 text-center">
        &copy; 2021 ChatDev. All rights reserved.
      </footer>
    </div>
  );
};
export default LandingPage;