package controllers

import play.api.mvc._

object Application extends Controller {

  def index = Action {
    Ok(views.html.index("Your new application is ready."))
  }

  def ping = Action { Request =>
    Ok(s"I think you table is available right now ${Request.body.asText}")

  }

}