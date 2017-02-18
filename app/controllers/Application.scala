package controllers

import play.api.mvc._

object Application extends Controller {

  def index = Action {
    Ok(views.html.index("Welcome to Ping Pong App!"))
  }

  def ping = Action { Request =>
    println(Request.body.asText)
    Ok("I think your table is available right now")

  }

}