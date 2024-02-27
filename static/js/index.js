document.addEventListener("DOMContentLoaded", function () {
  const toggleInput = document.getElementById("toggleInput");
  const cipherSelector = document.querySelector(".cipherSelector");
  const fileInput = document.getElementById("inputFile");
  const textInput = document.getElementById("inputText");
  const affineKey = document.getElementById("affineKey");
  const normalKey = document.getElementById("key");
  const downloadButton = document.getElementById("output");

  // Hide file input by default
  toggleInput.addEventListener("change", function () {
    const fileInputChecked = toggleInput.checked;
    const cipherOptions = cipherSelector.options;

    if (fileInputChecked) {
      // Hide options other than "extendedVigenere" and "auto-key"
      if (cipherSelector.value !== "autokey") {
        cipherSelector.value = "extendedVigenere";
      }
      fileInput.style.display = "flex";
      textInput.style.display = "none";
      affineKey.style.display = "none";
      normalKey.style.display = "block";
      try {
        downloadButton.style.display = "block";
      } catch (error) {}

      for (let i = 0; i < cipherOptions.length; i++) {
        if (
          cipherOptions[i].value !== "extendedVigenere" &&
          cipherOptions[i].value !== "autokey"
        ) {
          cipherOptions[i].disabled = true;
        }
      }
    } else {
      // Show all options
      fileInput.style.display = "none";
      textInput.style.display = "block";
      affineKey.style.display = "none";
      normalKey.style.display = "block";

      try {
        downloadButton.style.display = "none";
      } catch (error) {}

      for (let i = 0; i < cipherOptions.length; i++) {
        cipherOptions[i].disabled = false;
      }
    }
  });

  // open file input when clicking on the text input
  fileInput.addEventListener("click", function () {
    fileInput.click();
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const dragArea = document.querySelector(".drag-area");
  const fileInput = dragArea.querySelector("input[type=file]");

  // Prevent default behavior for drag events
  ["dragenter", "dragover", "dragleave", "drop"].forEach((eventName) => {
    dragArea.addEventListener(eventName, preventDefaults, false);
  });

  // Highlight drag area when dragging over it
  ["dragenter", "dragover"].forEach((eventName) => {
    dragArea.addEventListener(eventName, highlight, false);
  });

  // Remove highlight when dragging leaves the drag area
  ["dragleave", "drop"].forEach((eventName) => {
    dragArea.addEventListener(eventName, unhighlight, false);
  });

  // Handle file drop
  dragArea.addEventListener("drop", handleDrop, false);

  // Open file input when browse button is clicked
  dragArea.querySelector(".button").addEventListener("click", function () {
    fileInput.click();

    // Update support text to the selected file
    fileInput.addEventListener("change", function () {
      updateSupportText(fileInput.files);
    });
  });

  // Handle file selection from input
  fileInput.addEventListener("change", handleFiles, false);

  // Function to prevent default behavior for drag events
  function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
  }

  // Function to highlight drag area
  function highlight() {
    dragArea.classList.add("highlight");
  }

  // Function to remove highlight from drag area
  function unhighlight() {
    dragArea.classList.remove("highlight");
  }

  // Function to handle file drop
  function handleDrop(e) {
    const dt = e.dataTransfer;
    const files = dt.files;
    handleFiles(files);

    fileInput.files = files;
    updateSupportText(files);
  }

  // Function to handle selected files
  function handleFiles(files) {
    // Handle the dropped files here
    console.log(files);
  }

  function updateSupportText(files) {
    const supportText = document.querySelector(".support");
    if (files.length > 0) {
      supportText.textContent = "File: " + files[0].name;
    } else {
      supportText.textContent = "Supports: Any";
    }
  }
});

document.addEventListener("DOMContentLoaded", function () {
  // if affine cipher is selected, show the a and b key
  const cipherSelector = document.querySelector(".cipherSelector");
  const affineKey = document.getElementById("affineKey");
  const normalKey = document.getElementById("key");
  const firstNumKey = document.getElementById("firstNumKey");
  const secondNumKey = document.getElementById("secondNumKey");

  cipherSelector.addEventListener("change", function () {
    if (cipherSelector.value === "affine" || cipherSelector.value === "product") {
      normalKey.style.display = "none";
      affineKey.style.display = "flex";
      affineKey.style.flexDirection = "row";
      affineKey.style.gap = "12px";
      if (cipherSelector.value === "product") {
        firstNumKey.textContent = "Shifter";
        secondNumKey.textContent = "Key";
      } else {
        firstNumKey.textContent = "Multiplier (m)";
        secondNumKey.textContent = "Shifter (b)";
      }
    } else {
      normalKey.style.display = "block";
      affineKey.style.display = "none";
    }

  });
});