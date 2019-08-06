var xmlhttp, text;
xmlhttp = new XMLHttpRequest();
xmlhttp.open('GET', 'https://www.w3.org/TR/PNG/iso_8859-1.txt', false);
xmlhttp.send();
text = xmlhttp.responseText;
console.log(text)
document.getElementById('textread').innerHTML = text;


var rawFile = new XMLHttpRequest();
    rawFile.open("GET", 'file:///Users/sankeernalk/Desktop/hackathon/sum.txt', false);
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


    const logFileText = async file => {
    const response = await fetch(file)
    const text = await response.text()
    console.log(text)
}

logFileText('sum.txt')


var xmlhttp, text;
xmlhttp = new XMLHttpRequest();
xmlhttp.open('GET', 'https://www.w3.org/TR/PNG/iso_8859-1.txt', false);
xmlhttp.send();
text = xmlhttp.responseText;
console.log(text)
document.getElementById('textread').innerHTML = text;


<base href="file:///Users/sankeernalk/Desktop/hackathon/"/>
  <script>
    window.onload = function(){
    var iframe = document.createElement('iframe');
    iframe.id = 'iframe';
    iframe.style.display = 'none';
    document.body.appendChild(iframe);
    iframe.src = 'sum.txt';
    setTimeout(function(){
        var text = document.getElementById('iframe').contentDocument.body.firstChild.innerHTML;
        alert(text);
        console.log(text)
    }, 1000);
}
</script>



var file = new File([],"/Users/sankeernalk/Desktop/hackathon/sum.txt");
console.log(file.name)
var reader = new FileReader();
reader.onload = function(e) {  
  bfile = e.target.result 
  alert(bfile);   // this shows bfile
}
var x = reader.readAsText(file)
console.log(x.result)


var rawFile = new XMLHttpRequest();
    rawFile.open("GET", 'http://127.0.0.1:5000/sum.txt', false);
    rawFile.onreadystatechange = function ()
    {
        console.log("hi")
        if(rawFile.readyState === 4)
        {
        console.log("hi1")
            if(rawFile.status === 200 || rawFile.status == 0)
            {
        console.log("hi2")
                var allText = rawFile.responseText;
                console.log(typeof(allText))
                document.getElementById('textread').innerHTML = allText;
                console.log(allText)
            }
        }
    }
    rawFile.send(null);
    console.log("exit")


input.onchange = function(){
  var sound = document.getElementById('sound');
  var reader = new FileReader();
  reader.onload = function(e) {
    sound.src = this.result;
    sound.controls = true;
    sound.play();
    };
  reader.readAsDataURL(this.files[0]);
}