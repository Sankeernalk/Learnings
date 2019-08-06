var rawFile = new XMLHttpRequest();
    rawFile.open("GET", 'https://raw.githubusercontent.com/Sankeernalk/GitFirstRepository/master/summary_momeric.txt', false);
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                var allText = rawFile.responseText;
                document.getElementById('textread').innerHTML = allText;
                console.log(allText)
            }
        }
    }
    rawFile.send(null);
    console.log("exit")