// Определение массива картинок для фона
var images = [
  "{% static 'myapp1/images/image1.jpg' %}",
  "{% static 'myapp1/images/image2.jpg' %}",
  "{% static 'myapp1/images/image3.jpg' %}"
];

var index = 0;
var backgroundImage = document.getElementById("background-image");

// Функция для смены фона с помощью следующей картинки в массиве
function changeBackground() {
  backgroundImage.style.opacity = 0; // Плавное исчезновение текущего фона

  setTimeout(function() {
    index = (index + 1) % images.length; // Вычисление индекса следующей картинки
    backgroundImage.src = images[index]; // Установка следующей картинки

    backgroundImage.style.opacity = 1; // Плавное появление нового фона
  }, 500); // Задержка перед сменой фона (в данном случае, полсекунды)
}

// Вызов функции смены фона через определенный интервал
setInterval(changeBackground, 5000); // Смена фона каждые 5 секунд
