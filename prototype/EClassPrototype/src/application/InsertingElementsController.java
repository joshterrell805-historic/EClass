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

public class InsertingElementsController implements Initializable {

    @FXML
    public static Button button_image; // Value injected by FXMLLoader

    @FXML
    public static Button button_delete; // Value injected by FXMLLoader

    @FXML
    public static Button button_textbox; // Value injected by FXMLLoader

    @FXML
    public static Button button_list; // Value injected by FXMLLoader

    @FXML
    public static ScrollPane webview; // Value injected by FXMLLoader

    @FXML
    public static Button button_slidify; // Value injected by FXMLLoader

    @FXML
    public static Pane buttonpane; // Value injected by FXMLLoader

    @FXML
    public static TextArea done_textbox; // Value injected by FXMLLoader

    @FXML
    public static TextArea done_list; // Value injected by FXMLLoader

    @FXML
    public static ImageView done_image; // Value injected by FXMLLoader

    @Override
    public void initialize(URL fxmlFileLocation, final ResourceBundle resources)
    {
      Globals.insertingElementsController = this;

      done_textbox.setVisible(false);
      done_textbox.setEditable(false);
      done_textbox.setText("The Software Development Process");
      done_list.setVisible(false);
      done_list.setEditable(false);
      done_list.setText("A. For software to be properly engineered, its development must be conducted in an orderly process.\n   (unorderly projects become very difficult to manage)\nB. The diagram in the figure below depicts the major stages of the software development process.");
      done_image.setVisible(false);

      button_image.setOnAction(new EventHandler<ActionEvent>()
      {
         public void handle(ActionEvent event)
         {
            clickButtonImage();
         }
      });

      button_textbox.setOnAction(new EventHandler<ActionEvent>()
      {
         public void handle(ActionEvent event)
         {
            clickButtonTextbox();
         }
      });

      button_delete.setOnAction(new EventHandler<ActionEvent>()
      {
         public void handle(ActionEvent event)
         {
            clickButtonDelete();
         }
      });

      button_list.setOnAction(new EventHandler<ActionEvent>()
      {
         public void handle(ActionEvent event)
         {
            clickButtonList();
         }
      });

      done_image.setOnMouseClicked(new EventHandler<MouseEvent>()
      {
         public void handle(MouseEvent event)
         {
            if (selectedButton == button_delete)
               done_image.setVisible(false);
         }
      });
      done_list.setOnMouseClicked(new EventHandler<MouseEvent>()
      {
         public void handle(MouseEvent event)
         {
            if (selectedButton == button_delete)
               done_list.setVisible(false);
         }
      });
      done_textbox.setOnMouseClicked(new EventHandler<MouseEvent>()
      {
         public void handle(MouseEvent event)
         {
            if (selectedButton == button_delete)
               done_textbox.setVisible(false);
         }
      });

      webview.setOnMouseClicked(new EventHandler<MouseEvent>()
      {
         public void handle(MouseEvent event)
         {
            clickWebview();
         }
      });

      buttonpane.setOnMouseClicked(new EventHandler<MouseEvent>()
      {
         public void handle(MouseEvent event)
         {
            clickButtonpane();
         }
      });

      button_slidify.setOnAction(new EventHandler<ActionEvent>()
      {
         public void handle(ActionEvent event)
         {
            clickButtonSlidify();
         }
      });
    }

    private Button selectedButton = null;

    public void clickButtonImage()
    {
      if (selectedButton != null)
         selectedButton.setStyle("");
      selectedButton = button_image;
      selectedButton.setStyle("-fx-background-color: yellow;");
    }

    public void clickButtonTextbox()
    {
      if (selectedButton != null)
         selectedButton.setStyle("");
      selectedButton = button_textbox;
      selectedButton.setStyle("-fx-background-color: yellow;");
    }

    public void clickButtonList()
    {
      if (selectedButton != null)
         selectedButton.setStyle("");
      selectedButton = button_list;
      selectedButton.setStyle("-fx-background-color: yellow;");
    }

    public void clickWebview()
    {
      Parent root = null;

      try {
         String fxml = null;
         String title = null;

         if (selectedButton == null)
         {
         }
         else if (selectedButton == button_image)
         {
            done_image.setVisible(true);
         }
         else if (selectedButton == button_textbox)
         {
            fxml = "specify-text.fxml";
            title = "Specify Text";
         }
         else if (selectedButton == button_list)
         {
            fxml = "specify-list.fxml";
            title = "Specify List";
         }

         if (fxml != null)
         {
            root = FXMLLoader.load(getClass().getResource(fxml));
            Stage stage = new Stage();
            stage.setScene(new Scene(root, 600, 400));
            stage.setTitle(title);
            stage.show();
         }
      } catch (IOException e) {
         e.printStackTrace();
      }

    }

    public void clickButtonpane()
    {
      if (selectedButton != null)
      {
         selectedButton.setStyle("");
         selectedButton = null;
      }
    }

    public void clickButtonSlidify()
    {
      try {
         Parent root = FXMLLoader.load(getClass().getResource("slidify.fxml"));
         Stage stage = new Stage();
         stage.setScene(new Scene(root, 600, 400));
         stage.setTitle("Slidify");
         stage.show();
      } catch (IOException e) {
         e.printStackTrace();
      }
    }

    public void clickButtonDelete()
    {
      if (selectedButton != null)
         selectedButton.setStyle("");
      selectedButton = button_delete;
      selectedButton.setStyle("-fx-background-color: yellow;");
    }

    public void showList()
    {
      done_list.setVisible(true);
    }

}
