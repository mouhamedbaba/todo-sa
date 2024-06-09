$(document).ready(function () {
  if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    document.getElementById("dark-icon").classList.remove("scale-0")
  } else { 
    document.getElementById("light-icon").classList.remove("scale-0") 
  }
});


const ToggleTheme = () => {
  document.getElementById("dark-icon").classList.toggle('scale-0');
  document.getElementById("light-icon").classList.toggle('scale-0');


  if (localStorage.getItem('color-theme')) {
    if (localStorage.getItem('color-theme') === 'light') {
        document.documentElement.classList.add('dark');
        localStorage.setItem('color-theme', 'dark');
    } else {
        document.documentElement.classList.remove('dark');
        localStorage.setItem('color-theme', 'light');
    }
} else {
    if (document.documentElement.classList.contains('dark')) {
        document.documentElement.classList.remove('dark');
        localStorage.setItem('color-theme', 'light');
    } else {
        document.documentElement.classList.add('dark');
        localStorage.setItem('color-theme', 'dark');
    }
}
}