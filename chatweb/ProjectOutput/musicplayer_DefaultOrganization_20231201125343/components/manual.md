# Music Player User Manual

## Introduction

The Music Player is a web-based application developed by ChatDev that allows you to play and display your mp3 files. It provides a user-friendly interface with buttons for skipping songs, going back to the previous song, and pausing and playing songs using icons. This user manual will guide you through the installation process and explain how to use the Music Player effectively.

## Installation

To use the Music Player, you need to have the following dependencies installed:

- Next JS
- TypeScript
- Tailwind CSS
- React Icons

Follow these steps to install the dependencies and set up the environment:

1. Make sure you have Node.js installed on your machine. You can download it from the official website: [https://nodejs.org](https://nodejs.org)

2. Open a terminal or command prompt and navigate to the directory where you want to install the Music Player.

3. Run the following command to create a new Next.js project:

   ```
   npx create-next-app music-player
   ```

4. Change into the project directory:

   ```
   cd music-player
   ```

5. Install the required dependencies:

   ```
   npm install typescript tailwindcss react-icons
   ```

6. Create a `tailwind.config.js` file in the root of your project with the following content:

   ```javascript
   module.exports = {
     purge: [],
     darkMode: false, // or 'media' or 'class'
     theme: {
       extend: {},
     },
     variants: {
       extend: {},
     },
     plugins: [],
   };
   ```

7. Create a `postcss.config.js` file in the root of your project with the following content:

   ```javascript
   module.exports = {
     plugins: {
       tailwindcss: {},
       autoprefixer: {},
     },
   };
   ```

8. Create a `tsconfig.json` file in the root of your project with the following content:

   ```json
   {
     "compilerOptions": {
       "target": "es5",
       "lib": ["dom", "dom.iterable", "esnext"],
       "allowJs": true,
       "skipLibCheck": true,
       "strict": false,
       "forceConsistentCasingInFileNames": true,
       "noEmit": true,
       "esModuleInterop": true,
       "module": "esnext",
       "moduleResolution": "node",
       "resolveJsonModule": true,
       "isolatedModules": true,
       "jsx": "preserve"
     },
     "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx"],
     "exclude": ["node_modules"]
   }
   ```

9. Replace the contents of the `pages/index.js` file with the following code:

   ```tsx
   import Main from '../components/main';

   export default function Home() {
     return <Main />;
   }
   ```

10. Create a new directory called `components` in the root of your project.

11. Create three new files inside the `components` directory: `main.tsx`, `player.tsx`, and `songlist.tsx`.

12. Copy and paste the code provided in the task description into their respective files.

13. Your project structure should now look like this:

    ```
    music-player/
    ├── components/
    │   ├── main.tsx
    │   ├── player.tsx
    │   └── songlist.tsx
    ├── pages/
    │   └── index.tsx
    ├── postcss.config.js
    ├── tailwind.config.js
    └── tsconfig.json
    ```

14. Start the development server:

    ```
    npm run dev
    ```

15. Open your web browser and navigate to [http://localhost:3000](http://localhost:3000) to access the Music Player.

## Using the Music Player

Once you have installed and set up the Music Player, you can start using it to play and display your mp3 files. Here are the main functions and how to use them:

### Song Selection

- By default, the Music Player will display the first song in the list. To select a different song, click on the song title in the Song List on the right side of the player.

### Play/Pause

- To play or pause the current song, click on the play/pause button in the center of the player. The button will change between the play and pause icons depending on the current state.

### Skip Song

- To skip to the next song in the list, click on the skip song button on the right side of the player. This will play the next song in the list.

### Go Back Song

- To go back to the previous song in the list, click on the go back song button on the left side of the player. This will play the previous song in the list.

### Song Progress

- The progress bar at the bottom of the player shows the current progress of the song. You can click and drag the slider to jump to a specific time in the song.

### Song List

- To view the full list of songs, click on the music icon button at the bottom right corner of the player. This will expand the Song List on the right side of the player.

- Click on any song in the Song List to select and play it.

## Conclusion

Congratulations! You have successfully installed and learned how to use the Music Player developed by ChatDev. Enjoy playing and displaying your mp3 files with ease. If you have any further questions or need assistance, please don't hesitate to contact our support team.