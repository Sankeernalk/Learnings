const sendMail = async () => {
  console.log('hi 1')
  alert("Sending mail")
  const response = await fetch('http://127.0.0.1:5000/');
  alert("Mail sent successfully")
  console.log('hi')
}