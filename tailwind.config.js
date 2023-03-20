/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./campuvista/**/*.{html,js}",
    "./src/**/*.{html,js}",
    "./node_modules/tw-elements/dist/js/**/*.js"    
],
  theme: {
    extend: {},
  },
  plugins: [require("tw-elements/dist/plugin")],
}
