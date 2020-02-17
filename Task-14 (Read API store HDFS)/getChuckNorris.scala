import java.io.{File, PrintWriter}
import java.net.{HttpURLConnection, URL, URLConnection}

object getChuckNorris {
  def main(args: Array[String]): Unit = {
    val url: URL = new URL("https://api.chucknorris.io/jokes/random")

    val conn: URLConnection = url.openConnection
    conn.addRequestProperty("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36 Edg/79.0.309.43");
    print("conn: " + conn.getClass + "\n")

    val input_stream = conn.getInputStream
    val content = io.Source.fromInputStream(input_stream).mkString

    input_stream.close

    val local_path = "scalaData.json"

    val local_writer = new PrintWriter(new File(local_path))
    local_writer.write(content)
    local_writer.close
  }
}
