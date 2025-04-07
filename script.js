document.getElementById("cpf").addEventListener("input", function (e) {
  let value = e.target.value.replace(/\D/g, ""); // Remove tudo que não for número
  if (value.length > 11) value = value.slice(0, 11); // Limita a 11 dígitos

  // Formata como CPF (###.###.###-##)
  if (value.length > 9) {
    e.target.value = `${value.slice(0, 3)}.${value.slice(3, 6)}.${value.slice(
      6,
      9
    )}-${value.slice(9, 11)}`;
  } else if (value.length > 6) {
    e.target.value = `${value.slice(0, 3)}.${value.slice(3, 6)}.${value.slice(
      6
    )}`;
  } else if (value.length > 3) {
    e.target.value = `${value.slice(0, 3)}.${value.slice(3)}`;
  } else {
    e.target.value = value;
  }
});
