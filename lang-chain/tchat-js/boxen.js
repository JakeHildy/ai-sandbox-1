import boxen from "boxen";

const customBoxen = (str, title = "User", variant = "user") => {
  let width = 30;
  if (str.length < 40) {
    width = 40;
  } else if (str.length > 70) {
    width = 70;
  } else {
    width = str.length;
  }

  console.log(
    boxen(str, {
      title,
      borderColor: variant === "user" ? "green" : "blue",
      borderStyle: "round",
      padding: 0,
      margin: 0,
      titleAlignment: "center",
      float: variant === "user" ? "left" : "right",
      width,
    })
  );
};

export default customBoxen;
