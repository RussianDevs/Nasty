const showOrHidePassword = () => {
  const password = document.getElementById('password');
  if (password.type === 'password') {
    password.type = 'text';
  } else {
    password.type = 'password';
  }
};

show_password.checked = false;
show_password.addEventListener('change', showOrHidePassword);