/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../templates/**/*.html',       // Global templates folder
    '../**/templates/**/*.html',    // App-specific templates
  ],
  theme: {
    extend: {
      letterSpacing: {
        'wide': '0.8em',
        'tight': '0.2em',
      },
      backgroundImage: {
        'back-img-main': "url('/static/Images/hotel2.jpg')",
      }
    },
  },
  plugins: [
    require('daisyui'),
  ],
}

