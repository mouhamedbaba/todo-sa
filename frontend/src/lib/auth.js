const getUser = () =>{
  const user = localStorage.getItem("user")
  if (user) {
      return JSON.stringify(user)
  }else{
    return null
  }
}

const SetUser = (user) =>{
  if (user){
    localStorage.setItem("user", JSON.parse(user))
  }
}

