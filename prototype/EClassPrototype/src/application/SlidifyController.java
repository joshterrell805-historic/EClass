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

public class SlidifyController implements Initializable
{

   @FXML
   public static Parent root; // Value injected by FXMLLoader 
   @FXML
   public static Button buttonOk; // Value injected by FXMLLoader
   @FXML
   public static Button buttonSlidify; // Value injected by FXMLLoader
   @FXML
   public static Separator upperBR; // Value injected by FXMLLoader
   @FXML
   public static Separator lowerBR; // Value injected by FXMLLoader
   @FXML
   public static ImageView scrollableIcon; // Value injected by FXMLLoader
   @FXML
   public static Pane doubleClickMe; // Value injected by FXMLLoader

   boolean dragging = false;
   double yMouseStart;

   @Override
   public void initialize(URL fxmlFileLocation, final ResourceBundle resources)
   {
      root.setOnKeyPressed(new EventHandler<KeyEvent>()
      {
          @Override
          public void handle(KeyEvent ke)
          {
              if (ke.getCode().equals(KeyCode.DELETE))
              {
                  deleteBR(); 
              }
          }
      }); 

      lowerBR.setVisible(false);
      upperBR.setVisible(false);
      doubleClickMe.setVisible(true);
      scrollableIcon.setVisible(false);

      buttonOk.setOnAction(new EventHandler<ActionEvent>()
      {
         public void handle(ActionEvent event)
         {
            ((Stage)root.getScene().getWindow()).close();
         }
      });
      buttonSlidify.setOnAction(new EventHandler<ActionEvent>()
      {
         public void handle(ActionEvent event)
         {
            slidify();
         }
      });
      
      doubleClickMe.setOnMouseClicked(new EventHandler<MouseEvent>() {
          @Override
          public void handle(MouseEvent mouseEvent) {
              if(mouseEvent.getButton().equals(MouseButton.PRIMARY)
                  && mouseEvent.getClickCount() == 2){

                  lowerBR.setVisible(true);
                  doubleClickMe.setVisible(false);
                  scrollableIcon.setVisible(false);
              }
          }
      });
      lowerBR.setOnMousePressed(new EventHandler<MouseEvent>() {
        @Override public void handle(MouseEvent mouseEvent) {
         if (lowerBR.isVisible() && !upperBR.isVisible())
         {
            dragging = true;
            yMouseStart = mouseEvent.getSceneY();
         }
        }
      });
      lowerBR.setOnMouseReleased(new EventHandler<MouseEvent>() {
        @Override public void handle(MouseEvent mouseEvent) {

         if(dragging && mouseEvent.getSceneY() - yMouseStart < 25
            && lowerBR.isVisible() && !upperBR.isVisible())
         {
            upperBR.setVisible(true);
            lowerBR.setVisible(false);
            doubleClickMe.setVisible(true);
            scrollableIcon.setVisible(true);

         }
         dragging = false;
        }
      });
      upperBR.setOnMousePressed(new EventHandler<MouseEvent>() {
        @Override public void handle(MouseEvent mouseEvent) {
         if (!lowerBR.isVisible() && upperBR.isVisible())
         {
            dragging = true;
            yMouseStart = mouseEvent.getSceneY();
         }
        }
      });
      upperBR.setOnMouseReleased(new EventHandler<MouseEvent>() {
        @Override public void handle(MouseEvent mouseEvent) {

         if(dragging && mouseEvent.getSceneY() - yMouseStart > 25
            && !lowerBR.isVisible() && upperBR.isVisible())
         {
            upperBR.setVisible(false);
            lowerBR.setVisible(true);
            doubleClickMe.setVisible(false);
            scrollableIcon.setVisible(false);
         }
         dragging = false;
        }
      });
   }

   public void slidify()
   {
      lowerBR.setVisible(true);
      doubleClickMe.setVisible(false);
   }
   public void deleteBR()
   {
      if (upperBR.isVisible())
      {
         upperBR.setVisible(false);
      }
      else if (lowerBR.isVisible())
      {
         lowerBR.setVisible(false);
         doubleClickMe.setVisible(true);
      }
   }
}
