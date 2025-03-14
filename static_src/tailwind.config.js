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
      },
      colors:{
        'oxblood':'#622021',
        'crimson':'#991B20',
        'egypt':'#E1CAA5',
        'seafoam':'#FEF9DE',
      }
    },
  },
  plugins: [
    require('daisyui'),
  ],
}

