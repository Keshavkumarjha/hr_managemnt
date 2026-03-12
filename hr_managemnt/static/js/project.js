/* Project specific Javascript goes here. */
document.addEventListener("DOMContentLoaded", () => {
  const drawerBtn = document.getElementById("hr-sidebar-toggle");
  const drawer = document.getElementById("hr-sidebar");

  if (drawerBtn && drawer) {
    drawerBtn.addEventListener("click", () => {
      drawer.classList.toggle("hidden");
    });
  }
});
