// THIS CODE EXIST SO THAT I CAN ONLY HAVE ONE MODAL ON THE BASE TEMPLATE.
// THIS MEANS THAT i DONT HAVE TO CLOG ALL OTHE TEMPLATES WITH MODALS
// THE JS CODE COLLECTS DATA WHEN BUTTON IS CLICKED, IT COLLECTS MESSAGE AND DJANGO URL LINK

// Add a click event listener to each button that collects the data 
// from the button and passes it to the modal.
const confirmBtns = document.querySelectorAll('.confirm-btn');

confirmBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    const title = btn.dataset.title;
    // const message = btn.dataset.message;
    const id =btn.dataset.id;
    const msg = btn.dataset.msg;
    const url = btn.dataset.url;
    const button = btn.dataset.button;
    console.log(msg)
    // Set the message based on the id
    //  it will be easier to set the message from here since many depend on it
    if (id === 'edit') {
      message = 'Once you edit it, original content will be lost.';
    } else if (id === 'hide') {
      message = 'Once you hide it will not be available for other.';
    } 
    else if(id === 'msg'){ // this one looks for the ones with message set by thnl
      message = msg
    }
    else if(id === 'delete'){
      message = msg
    }
    else { //looks for the ones that hev no message and no id
      message = 'Are you sure you want to perform this action?';
    }

    showModal(title, message, url, button);
  });
});



// Update the showModal function to replace the placeholders with the collected data.
function showModal(title, message, url, button) {
    const modal = document.getElementById('confirm-modal');
    const modalTitle = document.getElementById('confirm-modal-title');
    const messageElem = document.getElementById('confirm-message');
    const confirmBtn = document.getElementById('confirm-btn');
    modalTitle.textContent = title; // Update the title if needed
    messageElem.textContent = message;
    confirmBtn.textContent = button;
    confirmBtn.addEventListener('click', () => {
      window.location.href = url;
    });
  
    // display the modal
    const modalInstance = new bootstrap.Modal(modal, { // Create a new instance of the modal
      backdrop: 'static', // Prevent clicking outside the modal to close it
      keyboard: false // Prevent pressing "escape" to close the modal
    });
    modalInstance.show(); // Show the modal
  }
  
