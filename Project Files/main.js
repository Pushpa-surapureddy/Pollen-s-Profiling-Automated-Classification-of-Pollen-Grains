document.addEventListener("DOMContentLoaded", () => {
  const fileInput = document.getElementById("image-upload");
  if (fileInput) {
    fileInput.addEventListener("change", () => {
      console.log(`Selected file: ${fileInput.files[0]?.name}`);
    });
  }
});
