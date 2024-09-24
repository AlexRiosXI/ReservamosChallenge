let debounceTimer;

    const debounce = (callback, delay) => {
      clearTimeout(debounceTimer);
      debounceTimer = setTimeout(callback, delay);
    };

export default debounce;