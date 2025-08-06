document.addEventListener('DOMContentLoaded', () => {
    const startButton = document.getElementById('startButton');
    const startScreen = document.getElementById('start-screen');
    const loginScreen = document.getElementById('login-screen');
    const moduleButtonsContainer = document.getElementById('moduleButtonsContainer');
    const loginForm = document.getElementById('loginForm');
    const errorMessage = document.getElementById('errorMessage');

    // Başlat butonuna tıklandığında
    if (startButton) {
        startButton.addEventListener('click', () => {
            if (startScreen && loginScreen) {
                startScreen.classList.add('hidden');
                loginScreen.classList.remove('hidden');
            }
        });
    }

    // Giriş formuna submit olduğunda (gönderildiğinde)
    if (loginForm) {
        loginForm.addEventListener('submit', (e) => {
            e.preventDefault(); // Sayfanın yeniden yüklenmesini engelle
            
            const usernameInput = loginForm.querySelector('input[name="username"]').value;
            const passwordInput = loginForm.querySelector('input[name="password"]').value;
            
                if (loginScreen && moduleButtonsContainer) {
                    loginScreen.classList.add('hidden');
                    moduleButtonsContainer.classList.remove('hidden')
                     window.location.href = 'modules.html';
                }
             else {
                if (errorMessage) {
                    errorMessage.textContent = 'Kullanıcı adı veya şifre yanlış.';
                }
            }
        });
    }

    // İletişim Becerileri modül kartına tıklama olayını dinle
    const iletisimModule = document.getElementById('iletisimModule');
    if (iletisimModule) {
        iletisimModule.addEventListener('click', (e) => {
            // e.preventDefault(); // Eğer sayfa yönlendirmesi olmasını istemezseniz
            console.log('İletişim Becerileri modülüne tıklandı!');
        });
    }

    // Problem Çözme Becerileri modül kartına tıklama olayını dinle
    const problemModule = document.getElementById('problemModule');
    if (problemModule) {
        problemModule.addEventListener('click', (e) => {
            // e.preventDefault(); // Eğer sayfa yönlendirmesi olmasını istemezseniz
            console.log('Problem Çözme Becerileri modülüne tıklandı!');
        });
    }

    // Çizim Tahtası modül kartına tıklama olayını dinle
    const cizimModule = document.getElementById('cizimModule');
    if (cizimModule) {
        cizimModule.addEventListener('click', (e) => {
            // e.preventDefault(); // Eğer sayfa yönlendirmesi olmasını istemezseniz
            console.log('Çizim Tahtası modülüne tıklandı!');
        });
    }
});