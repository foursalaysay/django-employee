// Function to open the dialog
function openDialog() {
    document.getElementById('dialog').style.display = 'block';
  }
  
  // Function to close the dialog
  function closeDialog() {
    document.getElementById('dialog').style.display = 'none';
  }
  
  function updateTime() {
    const now = new Date();
    const hours = now.getHours();
    const minutes = now.getMinutes();
    const seconds = now.getSeconds();
  
    const formattedTime = `${hours < 10 ? '0' + hours : hours}:${minutes < 10 ? '0' + minutes : minutes}:${seconds < 10 ? '0' + seconds : seconds}`;
  
    document.getElementById('currentTime').textContent = formattedTime;
  }
  
  // Call updateTime function every second to update the time
  setInterval(updateTime, 1000);
  
  // Initial call to display the time immediately when the page loads
  updateTime();  