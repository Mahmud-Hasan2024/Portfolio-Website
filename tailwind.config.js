module.exports = {
  content: [
    "./templates/**/*.html",
    "./**/*.js",
  ],
  theme: {
    extend: {
      colors: {
        primary_bg: "#0F1419",
        secondary_bg: "#1A2332",
        accent: "#E8914C",
        text_primary: "#E8E8E8",
        text_secondary: "#A0A0A0",
      }
    },
  },
  plugins: [
    require('daisyui'),
  ],
}
