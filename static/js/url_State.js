window.addEventListener('popstate', function(event) {
    // Retrieve the state object and update the page accordingly
    const state = event.state;
    if (state) {
        window.scrollTo(0, state.scrollPosition);
    }
});
