package controllers

import play.api.data.{Form, Forms}
import play.api.mvc.{Action, Controller}

object Commands extends Controller {

  def ping = Action { Request =>
    println(Request.queryString get "team_domain")
    Ok("I think your table is available right now")
  }
}
