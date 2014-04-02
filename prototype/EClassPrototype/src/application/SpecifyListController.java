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
import javafx.scene.control.*;
import javafx.stage.Stage;
import javafx.scene.web.WebView;
import javafx.scene.input.*;
import javafx.scene.layout.*;

public class SpecifyListController implements Initializable {

    @FXML
    public static Parent root; // Value injected by FXMLLoader
    @FXML
    public static Button button_ok; // Value injected by FXMLLoader
    @FXML
    public static Button button_insert; // Value injected by FXMLLoader
    @FXML
    public static Button button_remove; // Value injected by FXMLLoader
    @FXML
    public static Button button_edit; // Value injected by FXMLLoader
    @FXML
    public static Label theElementText;
    @FXML
    public static Label theElementInnerTypeText;
    @FXML
    public static Pane theElement;
    @FXML
    public static MenuItem menuitem_sym1;
    @FXML
    public static MenuItem menuitem_sym2;
    @FXML
    public static MenuItem menuitem_sym3;
    @FXML
    public static MenuItem menuitem_sym4;
    @FXML
    public static MenuItem menuitem_sym5;
    @FXML
    public static MenuItem menuitem_sym6;
    @FXML
    public static MenuItem menuitem_sym7;
    @FXML
    public static MenuButton menubutton_sym;

    @Override
    public void initialize(URL fxmlFileLocation, final ResourceBundle resources)
    {
      theElement.setVisible(false);
      Globals.specifyListController = this;

      button_insert.setOnAction(new EventHandler<ActionEvent>()
      {
         public void handle(ActionEvent event)
         {
            clickButtonInsert();
         }
      });
      button_remove.setOnAction(new EventHandler<ActionEvent>()
      {
         public void handle(ActionEvent event)
         {
            clickButtonRemove();
         }
      });
      button_edit.setOnAction(new EventHandler<ActionEvent>()
      {
         public void handle(ActionEvent event)
         {
            clickButtonEdit();
         }
      });
      button_ok.setOnAction(new EventHandler<ActionEvent>()
      {
         public void handle(ActionEvent event)
         {
            Globals.insertingElementsController.showList();
            ((Stage)root.getScene().getWindow()).close();
         }
      });

      menuitem_sym7.setOnAction(new EventHandler<ActionEvent>(){
         public void handle(ActionEvent event){
         menubutton_sym.setText(menuitem_sym7.getText());}});
      menuitem_sym1.setOnAction(new EventHandler<ActionEvent>(){
         public void handle(ActionEvent event){
         menubutton_sym.setText(menuitem_sym1.getText());}});
      menuitem_sym2.setOnAction(new EventHandler<ActionEvent>(){
         public void handle(ActionEvent event){
         menubutton_sym.setText(menuitem_sym2.getText());}});
      menuitem_sym3.setOnAction(new EventHandler<ActionEvent>(){
         public void handle(ActionEvent event){
         menubutton_sym.setText(menuitem_sym3.getText());}});
      menuitem_sym4.setOnAction(new EventHandler<ActionEvent>(){
         public void handle(ActionEvent event){
         menubutton_sym.setText(menuitem_sym4.getText());}});
      menuitem_sym5.setOnAction(new EventHandler<ActionEvent>(){
         public void handle(ActionEvent event){
         menubutton_sym.setText(menuitem_sym5.getText());}});
      menuitem_sym6.setOnAction(new EventHandler<ActionEvent>(){
         public void handle(ActionEvent event){
         menubutton_sym.setText(menuitem_sym6.getText());}});
    }

    public void clickButtonEdit()
    {
      isEdit = true;
      try
      {
         Parent root = FXMLLoader.load(getClass().getResource("specify-element.fxml"));
         Stage stage = new Stage();
         stage.setScene(new Scene(root, 600, 450));
         stage.setTitle("Edit Element");
         stage.show();
      } catch (IOException e) {
         e.printStackTrace();
      }
    }
    public void clickButtonRemove()
    {
      theElement.setVisible(false);
    }
    public void clickButtonInsert()
    {
      isEdit = false;
      try
      {
         Parent root = FXMLLoader.load(getClass().getResource("specify-element.fxml"));
         Stage stage = new Stage();
         stage.setScene(new Scene(root, 600, 450));
         stage.setTitle("Insert Element");
         stage.show();
      } catch (IOException e) {
         e.printStackTrace();
      }
    }
    public void setElementAttributes(String elementText, String elementTypeText)
    {
      theElementText.setText(elementText);
      theElementInnerTypeText.setText(elementTypeText);
      theElement.setVisible(true);
    }
   
    public boolean isEdit = false;

    public String getElementText()
    {
      return theElementText.getText();
    }
    public String getElementTypeText()
    {
      return theElementInnerTypeText.getText();
    }
}
