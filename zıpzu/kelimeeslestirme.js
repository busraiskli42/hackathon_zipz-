document.addEventListener('DOMContentLoaded', function() {
    const wordDisplay = document.getElementById('word-display');
    const pictureGrid = document.getElementById('picture-grid');
    const feedbackMessage = document.getElementById('feedback-message');

    // Kelime-resim çiftleri (kendi kelime ve resimlerinizi buraya ekleyin)
    const wordImagePairs = [
        { word: 'ELMA', image: 'elma.png' },
        { word: 'TOP', image: 'topc.png' },
        { word: 'KEDİ', image: 'kedi1.png' },
        { word: 'ARABA', image: 'araba.png' },
        { word: 'GÜNEŞ', image: 'gunes.png' },
        { word: 'FİL', image: 'fil.png' },
        { word: 'KÖPEK', image: 'kopek.png' },
        // Daha fazla çift ekleyebilirsiniz
    ];

    let availableWordPairs = [...wordImagePairs]; // Kullanılabilir kelime çiftlerini tutar
    let currentWordPair = null;

    function getRandomWordPair() {
        if (availableWordPairs.length === 0) {
            return null; // Tüm kelimeler kullanıldı
        }
        const randomIndex = Math.floor(Math.random() * availableWordPairs.length);
        const selectedPair = availableWordPairs[randomIndex];
        availableWordPairs.splice(randomIndex, 1); // Seçilen çifti kullanılabilir listeden çıkar
        return selectedPair;
    }

    function shuffleArray(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
        }
    }

    function createGameRound() {
        currentWordPair = getRandomWordPair();

        if (currentWordPair === null) {
            // Tüm kelimeler kullanıldı, oyun bitti
            wordDisplay.textContent = "Oyun Bitti!";
            feedbackMessage.textContent = "Tebrikler, tüm kelimeleri eşleştirdin! 🎉";
            feedbackMessage.className = 'correct';
            pictureGrid.innerHTML = ''; // Resim ızgarasını temizle
            return;
        }

        wordDisplay.textContent = currentWordPair.word;
        feedbackMessage.textContent = '';
        
        // Yanlış resimleri oluşturmak için diğer çiftleri seç
        const otherPairs = wordImagePairs.filter(pair => pair.word !== currentWordPair.word);
        shuffleArray(otherPairs);
        // Seçenekleri mevcut kelime çifti ve diğerlerinden 3 tanesiyle sınırla
        const choicePairs = [currentWordPair, ...otherPairs.slice(0, 3)]; 
        shuffleArray(choicePairs);

        // Resim ızgarasını temizle ve yeni resimleri ekle
        pictureGrid.innerHTML = '';
        choicePairs.forEach(pair => {
            const card = document.createElement('div');
            card.className = 'picture-card';
            card.dataset.word = pair.word;
            
            const img = document.createElement('img');
            // Resimlerin "assets" klasöründe olduğunu varsayalım
            img.src = `assets/${pair.image}`; 
            img.alt = pair.word;
            
            card.appendChild(img);
            pictureGrid.appendChild(card);
            
            card.addEventListener('click', handleGuess);
        });
    }

    function handleGuess(event) {
        const clickedCard = event.currentTarget;
        const guessedWord = clickedCard.dataset.word;
        
        if (guessedWord === currentWordPair.word) {
            feedbackMessage.textContent = 'Doğru!';
            feedbackMessage.className = 'correct';
            
            // Doğru cevaptan sonra yeni bir tur başlat
            setTimeout(() => {
                createGameRound();
            }, 1400); // 1.5 saniye sonra yeni tura geç
            
        } else {
            feedbackMessage.textContent = 'Tekrar dene.';
            feedbackMessage.className = 'incorrect';
            
            clickedCard.classList.add('incorrect-shake');
            setTimeout(() => {
                clickedCard.classList.remove('incorrect-shake');
            }, 500);
        }
    }

    // Oyunu başlat
    createGameRound();
});
