document.addEventListener("DOMContentLoaded", function () {
  const toggleInput = document.getElementById("toggleInput");
  const cipherSelector = document.querySelector(".cipherSelector");
  const fileInputArea = document.getElementById("inputFile");
  const textInput = document.getElementById("inputText");
  const downloadButton = document.getElementById("output");
  const supprotLabel = document.querySelector(".support");
  const fileInput = document.getElementById("file");
  

  // Hide file input by default
  toggleInput.addEventListener("change", function () {
    const fileInputAreaChecked = toggleInput.checked;

    if (fileInputAreaChecked) {
      textInput.style.display = "none";
      fileInputArea.style.display = "flex";
      try {
        downloadButton.style.display = "block";
      } catch (error) {}
      // Change file options to only accept txt if the cipher is not extended vigenere or autokey
      if (cipherSelector.value !== "extendedVigenere" && cipherSelector.value !== "autoKey") {
        fileInput.accept = ".txt";
        supprotLabel.textContent = "Supported file types: .txt";
      } else {
        // Accept all file types
        fileInput.accept = "*";
        supprotLabel.textContent = "Supported file types: all";
      }
    } else {
      textInput.style.display = "block";
      fileInputArea.style.display = "none";
      try {
        downloadButton.style.display = "none";
      } catch (error) {}
    }
  });

  cipherSelector.addEventListener("change", function () {
    // Change file options to only accept txt if the cipher is not extended vigenere or autokey
    if (cipherSelector.value !== "extendedVigenere" && cipherSelector.value !== "autoKey") {
      fileInput.accept = ".txt";
      supprotLabel.textContent = "Supported file types: .txt";
    } else {
      // Accept all file types
      fileInput.accept = "*";
      supprotLabel.textContent = "Supported file types: all";
    }
  });

  // open file input when clicking on the text input
  fileInputArea.addEventListener("click", function () {
    fileInputArea.click();
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const dragArea = document.querySelector(".drag-area");
  const fileInput = document.getElementById("file");
  const browseButton = document.getElementById("browseButton");

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
  browseButton.addEventListener("click", function () {
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
    const supportText = document.getElementById("inputFileSupport");
    if (files.length > 0) {
      supportText.textContent = "File: " + files[0].name;
    } else {
      cipherSelector = document.querySelector(".cipherSelector");
      if (cipherSelector.value !== "extendedVigenere" && cipherSelector.value !== "autoKey") {
        supportText.textContent = "Supported file types: .txt";
      } else {
        supportText.textContent = "Supported file types: all";
      }
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