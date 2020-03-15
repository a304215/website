import { LightningElement,track ,api,wire} from 'lwc';
import get_all_product from '@salesforce/apex/EditProduct.get_all_product';
import product_back from '@salesforce/apex/NewProductByDiscount.quote_back';
import quote_find_oppoid from '@salesforce/apex/NewProductByDiscount.quote_find_oppoid'
import get_all_oil from '@salesforce/apex/EditProduct.get_all_oil';
export default class Edit_product_quote extends LightningElement {
    @api recordId;
    @track edit_product = false;
    @track edit_product_display_list = [];
    @track edit_product_mix_str = [];
    @track opp_id = "";
    @track quote_id_list = [];
    @wire(quote_find_oppoid,{quoteid:'$recordId'})
    get_opp_id({error,data}){
        if(data){
            console.log("get_in")
            this.opp_id = data;
            console.log(this.opp_id);
        }else if(error){
            console.log(error);
        }
    }
    handleButtonSelect(){
        console.log("get in function");
        get_all_product({opp_id:this.opp_id})
        .then(result => {
            console.log(result);
            for(let i = 0 ; i < result.length;i++){
                this.edit_product_display_list[i] = {
                    name:result[i].Name,
                    quantity:result[i].Quantity.toString(),
                    unitprice:result[i].ListPrice.toFixed(2).toString(),
                    discount:result[i].Discount.toString(),
                    nameUrl:'/lightning/r/PricebookEntry/'+result[i].Id,
                    sale_price:result[i].UnitPrice.toFixed(2).toString(),
                    total:result[i].Total_Line_Item_Sales_Price__c.toFixed(2).toString(),
                    select_id :i.toString(),
                    OLI_Id : result[i].Id
                }
            }
            console.log("finish");
            console.log(this.edit_product_display_list);
            this.edit_product = true;
        })
        .catch(error => {
            this.error = error;
        });
    }
    quantity_save(event){
        const now_select = event.target.name;
        const now_quantity = event.target.value;
        var total = 0;
        console.log(now_select);
        console.log(now_quantity)
        for(let i =0 ; i < this.edit_product_display_list.length;i++){
            if(now_select===this.edit_product_display_list[i].select_id){
                this.edit_product_display_list[i].quantity = now_quantity;
                total = parseFloat(now_quantity)*parseFloat(this.edit_product_display_list[i].unitprice)*parseFloat(this.edit_product_display_list[i].discount)/100;
                this.edit_product_display_list[i].total = total.toFixed(2).toString();
            }
        }
    }
    discount_save(event){
        const now_select = event.target.name;
        const now_discount = event.target.value;
        var total = 0;
        var sale_price = 0 ;
        for(let i = 0 ;i< this.edit_product_display_list.length;i++){
            if(now_select===this.edit_product_display_list[i].select_id){
                this.edit_product_display_list[i].discount = now_discount;
                total = parseFloat(now_discount)/100*parseFloat(this.edit_product_display_list[i].unitprice)*parseFloat(this.edit_product_display_list[i].quantity);
                this.edit_product_display_list[i].total = total.toFixed(2).toString();
                sale_price = this.edit_product_display_list[i].unitprice*now_discount/100;
                this.edit_product_display_list[i].sale_price = sale_price.toFixed(2).toString();
            }
        }
    }
    edit_product_cancel(){
        this.edit_product = false;
    }
    edit_product_save(){
        //console.log("get in ");
        console.log(this.edit_product_display_list);
        this.edit_product_mix_str = [];
        get_all_oil({quote_id:this.recordId})
        .then(result => {
            this.quote_id_list = result;
        })
        .catch(error => {
            this.error = error;
        });
        for(let i = 0 ; i < this.edit_product_display_list.length;i++){
            this.edit_product_mix_str[i] = this.edit_product_display_list[i].sale_price+","+this.edit_product_display_list[i].quantity+","+this.edit_product_display_list[i].discount+","+this.quote_id_list[i].Id;
        }
        console.log(this.edit_product_mix_str);
        console.log("now get in the apex");
        product_back({products:this.edit_product_mix_str,quote_id:this.recordId,status:false})
        .then(result => {
            console.log(result);
            console.log(this.edit_product_display_list);
            this.edit_product = false;
        })
        .catch(error => {
            this.error = error;
        });
    }
}