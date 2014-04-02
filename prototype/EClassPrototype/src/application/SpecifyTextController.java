package application;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.stage.Stage;
import javafx.scene.web.WebView;
import javafx.scene.input.*;
import javafx.scene.layout.*;
import javafx.scene.control.*;
import javafx.scene.image.*;

public class SpecifyTextController implements Initializable {

   @FXML
   public static Parent root; // Value injected by FXMLLoader 
   @FXML
   public static Button button_ok; // Value injected by FXMLLoader

   @Override
   public void initialize(URL fxmlFileLocation, final ResourceBundle resources)
   {
      button_ok.setOnAction(new EventHandler<ActionEvent>()
      {
         public void handle(ActionEvent event)
         {
            Globals.insertingElementsController.done_textbox.setVisible(true);
            ((Stage)root.getScene().getWindow()).close();
         }
      });
   }
}
