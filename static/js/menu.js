

// Hamburger ikonunu ve menüyü seç
const menuToggle = document.querySelector('.menu-toggle'); 
const navLinks = document.querySelector('nav ul'); 

// ☰ ikonuna tıklanınca menüyü aç/kapat
menuToggle.addEventListener('click', () => {
  navLinks.classList.toggle('active'); 
});

// Sayfa yeniden boyutlandığında menüyü kapat (mobil → masaüstü geçişinde sorun olmasın)
window.addEventListener('resize', () => {
  if (window.innerWidth > 768) {
    navLinks.classList.remove('active'); 
  }
});