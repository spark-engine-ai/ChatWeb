# Social Media Profile Card User Manual

## Introduction

The Social Media Profile Card is a web application that allows users to display their social media profile information in a visually appealing and organized manner. It provides a profile card component that includes the user's profile picture, name, bio, and social media handles. Additionally, it includes components for displaying profile statistics, actions, posts, and comments.

## Installation

To use the Social Media Profile Card web application, you need to have the following dependencies installed:

- Next.js: A React framework for building web applications.
- TypeScript: A typed superset of JavaScript that compiles to plain JavaScript.
- Tailwind CSS: A utility-first CSS framework for rapidly building custom user interfaces.
- react-icons: A library of icons for React.

To install these dependencies, follow the steps below:

1. Install Node.js: Visit the official Node.js website (https://nodejs.org) and download the latest LTS version for your operating system. Follow the installation instructions provided.

2. Create a new project directory: Open your terminal or command prompt and navigate to the directory where you want to create your project.

3. Initialize a new Next.js project: Run the following command to create a new Next.js project:

   ```
   npx create-next-app my-profile-card
   ```

4. Install the required dependencies: Navigate to the project directory by running `cd my-profile-card` and then run the following command to install the required dependencies:

   ```
   npm install tailwindcss react-icons
   ```

5. Configure Tailwind CSS: Create a new file named `tailwind.config.js` in the root of your project directory and add the following content:

   ```javascript
   module.exports = {
     purge: [],
     darkMode: false,
     theme: {
       extend: {},
     },
     variants: {},
     plugins: [],
   };
   ```

6. Import Tailwind CSS styles: Open the `styles/globals.css` file in your project directory and add the following line at the top to import the Tailwind CSS styles:

   ```css
   @import 'tailwindcss/tailwind.css';
   ```

7. Start the development server: Run the following command to start the Next.js development server:

   ```
   npm run dev
   ```

   This will start the development server and you can access the web application at `http://localhost:3000`.

## Usage

To use the Social Media Profile Card web application, follow the steps below:

1. Open the `pages/index.tsx` file in your project directory.

2. Modify the `ProfileCard` component props to customize the profile information. You can provide an array of social media handles with names and URLs.

   ```tsx
   <ProfileCard
     socialMediaHandles={[
       { name: 'Twitter', url: 'https://twitter.com' },
       { name: 'Instagram', url: 'https://instagram.com' },
     ]}
   />
   ```

3. Customize the profile statistics, actions, posts, and comments by modifying the respective components (`ProfileStats`, `ProfileActions`, `PostCard`, `CommentCard`) in the `Main` component.

4. Save the file and the changes will be automatically reflected in the web application.

## Conclusion

The Social Media Profile Card web application provides an easy and customizable way to display social media profile information. By following the installation and usage instructions provided in this user manual, you can quickly set up and customize the web application to meet your specific needs. Enjoy showcasing your social media presence with the Social Media Profile Card!