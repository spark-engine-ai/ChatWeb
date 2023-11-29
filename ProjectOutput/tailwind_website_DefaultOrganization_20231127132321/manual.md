# Building a Website Landing Page with React and Tailwind

To build a website landing page using React and Tailwind, you will need to follow these steps:

## Step 1: Set up the project

1. Create a new directory for your project.
2. Open a terminal and navigate to the project directory.
3. Run the following command to initialize a new React project:

```shell
npx create-react-app landing-page
```

4. Once the project is created, navigate to the project directory:

```shell
cd landing-page
```

## Step 2: Install Tailwind CSS

1. Install Tailwind CSS and its dependencies by running the following command:

```shell
npm install tailwindcss
```

2. Create a `tailwind.config.js` file in the project directory with the following content:

```javascript
module.exports = {
  purge: [],
  darkMode: false,
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
```

## Step 3: Create the necessary files

1. Create an `_app.js` file in the `src` directory with the following content:

```javascript
import React from 'react';
import '../styles/index.css';

function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />;
}

export default MyApp;
```

2. Create an `index.html` file in the `public` directory with the following content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Landing Page</title>
  <link href="/styles/index.css" rel="stylesheet">
</head>
<body>
  <div id="root"></div>
  <script src="/src/index.js"></script>
</body>
</html>
```

## Step 4: Update the package.json file

1. Open the `package.json` file in the project directory.
2. Replace the content with the following:

```json
{
  "name": "landing-page",
  "version": "1.0.0",
  "description": "Website landing page built with React and Tailwind",
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "dependencies": {
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "tailwindcss": "^2.2.19"
  },
  "devDependencies": {
    "react-scripts": "^4.0.3"
  }
}
```

## Step 5: Start the development server

1. Open a terminal and navigate to the project directory.
2. Run the following command to start the development server:

```shell
npm start
```

3. Open your web browser and visit `http://localhost:3000` to see the landing page.

That's it! You have successfully built a website landing page using React and Tailwind. Feel free to customize the page by modifying the components and styles in the project.

If you have any further questions or need assistance, please don't hesitate to reach out.