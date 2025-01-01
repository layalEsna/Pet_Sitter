import { useFormik } from 'formik';
import * as Yup from 'yup';

function Appointment() {

    const appointmentForm = useFormik({
        initialValues: {
            pet_name: '',
            pet_type: '',
            date: '',
            duration: ''
        },
        validationSchema: Yup.object({
            pet_name: Yup.string(),
            pet_type: Yup.string()
                .required('Pet type is required.'),
            date: Yup.string()
                .required('Date is required'),
            duration: Yup.number()
                .required('Duration is required.')
        }),
        onSubmit: (values) => {
            console.log(`Form submitted, ${values}`)
        }
    })

    
}


export default Appointment