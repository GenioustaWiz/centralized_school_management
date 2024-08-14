  // Get all the elements that contain text on the page
  const elements = document.querySelectorAll('body *:not(script)');

  // Function to set the font size of an element
  const setFontSize = (element, size) => {
    element.style.fontSize = `${size}px`;
  };
  
  // Function to resize all text on the page based on screen size
  const resizeText = () => {
    // Get the current screen size
    const screenWidth = window.innerWidth;
  
    // Set the base font size based on screen size
    let baseSize;
    if (screenWidth >= 768) {
      baseSize = 16;
    } else {
      baseSize = 14;
    }
  
    // Loop through each element and set its font size
    elements.forEach((element) => {
      setFontSize(element, baseSize);
    });
  };
  
  // Call the resizeText function when the window is resized
  window.addEventListener('resize', resizeText);
  
  // Call the resizeText function on page load
  resizeText();