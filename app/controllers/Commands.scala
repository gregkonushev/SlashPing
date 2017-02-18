package controllers

import play.api.mvc.{Action, Controller}

/**
  * Created by Grigory Konushev on 2/17/17.
  */
object Commands extends Controller {

  def ping = Action { Request =>
    println(Request.body)
    Ok("I think your table is available right now")
  }
}
