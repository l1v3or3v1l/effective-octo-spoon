const promise1 = fetch('https://api.codetabs.com/v1/proxy?quest=rewardpaper.com/the-hindu-epaper-pdf/').then(response => response.text());

promise1.then((text) => {
    let num = text.search('https://drive.google.com/file/');
    if (num != -1) { 
        let url = text.substring(num, num+83);
        document.getElementById("drive_link").href=url;
        window.location.replace(url);
    }
});