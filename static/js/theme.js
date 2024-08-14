const toggleButton = document.getElementById('toggle-theme');
const themeIcon = document.getElementById('theme-icon');
const body = document.body;

toggleButton.addEventListener('click', () => {
    const currentTheme = body.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    body.setAttribute('data-theme', newTheme);
    updateThemeIcon(newTheme);
    saveThemeToLocalStorage(newTheme);  
    updateTextColors(newTheme); // Update text colors based on the theme
});

// Check for user's preferred color scheme
const preferredColorScheme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
const savedTheme = getThemeFromLocalStorage();

if (savedTheme) {
    body.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);
    updateTextColors(savedTheme); // Update text colors based on the theme
} else {
    body.setAttribute('data-theme', preferredColorScheme);
    updateThemeIcon(preferredColorScheme);
    updateTextColors(preferredColorScheme); // Update text colors based on the theme
}

function updateThemeIcon(theme) {
    themeIcon.innerHTML = theme === 'dark' ? '🌞' : '🌙';
}

function saveThemeToLocalStorage(theme) {
    localStorage.setItem('selected-theme', theme);
}

function getThemeFromLocalStorage() {
    return localStorage.getItem('selected-theme');
}

function updateTextColors(theme) {
    const textColorElements = document.querySelectorAll('.theme-text');

    for (let i = 0; i < textColorElements.length; i++) {
        const computedColor = getComputedStyle(textColorElements[i]).color;

        if (theme === 'dark' && computedColor === 'rgb(0, 0, 0)') {
            textColorElements[i].style.color = '#ffffff';
        } else if (theme === 'light' && computedColor === 'rgb(255, 255, 255)') {
            textColorElements[i].style.color = 'rgb(0, 0, 0)';
        }
    }
}




// const toggleButton = document.getElementById('toggle-theme');
// const themeIcon = document.getElementById('theme-icon');
// const body = document.body;

// toggleButton.addEventListener('click', () => {
//     const currentTheme = body.getAttribute('data-theme');
//     const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
//     body.setAttribute('data-theme', newTheme);
//     updateThemeIcon(newTheme);
//     saveThemeToLocalStorage(newTheme); // Save the theme preference
// });

// // Check for user's preferred color scheme
// const preferredColorScheme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
// const savedTheme = getThemeFromLocalStorage();

// if (savedTheme) {
//     body.setAttribute('data-theme', savedTheme);
//     updateThemeIcon(savedTheme);
// } else {
//     body.setAttribute('data-theme', preferredColorScheme);
//     updateThemeIcon(preferredColorScheme);
// }

// function updateThemeIcon(theme) {
//     themeIcon.innerHTML = theme === 'dark' ? '🌞' : '🌙' ;
// }

// function saveThemeToLocalStorage(theme) {
//     localStorage.setItem('selected-theme', theme);
//     // or use "sessionStorage" for data is cleared when the browser session ends
// }

// function getThemeFromLocalStorage() {
//     return localStorage.getItem('selected-theme');
// }
