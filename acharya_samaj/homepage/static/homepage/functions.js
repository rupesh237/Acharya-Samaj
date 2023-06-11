var slideIndex = 0;
        var slides = document.getElementsByClassName("slideshow")[0].getElementsByTagName("img");

        function showSlides() {
            for (var i = 0; i < slides.length; i++) {
                slides[i].style.transform = "translateX(" + (i - slideIndex) * 600 + "px)";
            }

            slideIndex++;

            if (slideIndex >= slides.length) {
                slideIndex = 0;
            }

            setTimeout(showSlides, 1000);
        }

        function prevSlide() {
            slideIndex--;

            if (slideIndex < 0) {
                slideIndex = slides.length - 1;
            }

            showSlides();
        }

        function nextSlide() {
            slideIndex++;

            if (slideIndex >= slides.length) {
                slideIndex = 0;
            }

            showSlides();
        }

        showSlides();